// Before: Massive View Controller — networking, parsing, formatting,
// and navigation all in one class.

import UIKit

class UserProfileViewController: UIViewController {
    @IBOutlet weak var nameLabel: UILabel!
    @IBOutlet weak var emailLabel: UILabel!
    @IBOutlet weak var avatarImageView: UIImageView!
    @IBOutlet weak var loadingSpinner: UIActivityIndicatorView!

    var userId: String!

    override func viewDidLoad() {
        super.viewDidLoad()
        loadingSpinner.startAnimating()

        // Networking
        let url = URL(string: "https://api.example.com/users/\(userId!)")!
        URLSession.shared.dataTask(with: url) { [weak self] data, _, error in
            guard let self = self else { return }

            if let error = error {
                DispatchQueue.main.async {
                    self.showError(error.localizedDescription)
                }
                return
            }

            // Parsing
            guard let data = data,
                  let json = try? JSONSerialization.jsonObject(with: data) as? [String: Any],
                  let name = json["name"] as? String,
                  let email = json["email"] as? String,
                  let avatarUrl = json["avatar_url"] as? String else {
                DispatchQueue.main.async {
                    self.showError("Invalid response")
                }
                return
            }

            // Formatting and UI update
            DispatchQueue.main.async {
                self.nameLabel.text = name.uppercased()
                self.emailLabel.text = email.lowercased()
                self.loadingSpinner.stopAnimating()

                // Another network call for avatar
                self.loadAvatar(avatarUrl)
            }
        }.resume()
    }

    func loadAvatar(_ urlString: String) {
        guard let url = URL(string: urlString) else { return }
        URLSession.shared.dataTask(with: url) { [weak self] data, _, _ in
            guard let data = data, let image = UIImage(data: data) else { return }
            DispatchQueue.main.async {
                self?.avatarImageView.image = image
            }
        }.resume()
    }

    func showError(_ message: String) {
        let alert = UIAlertController(title: "Error", message: message, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "OK", style: .default))
        present(alert, animated: true)
    }
}
