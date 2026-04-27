# Massive VC → MVVM + Coordinators

Refactored from a massive view controller to MVVM with a coordinator for navigation.

## Design Pressure

- `UserProfileViewController` handled networking, JSON parsing, formatting, and navigation.
- Network calls were inline — not testable without UI.
- Formatting logic (uppercased name, lowercased email) was coupled to the view.
- Navigation (showing alerts) was mixed with data loading.

## Applied Pattern

**MVVM + Coordinator** — extract data loading to a `ViewModel`, navigation to a `Coordinator`. The view controller only updates the UI.

## After Code

### `UserProfileViewModel.swift`

```swift
import Foundation

struct UserProfile {
    let displayName: String
    let email: String
    let avatarUrl: URL?
}

class UserProfileViewModel {
    private let userId: String
    private let apiClient: APIClient

    var onProfileLoaded: ((UserProfile) -> Void)?
    var onError: ((String) -> Void)?
    var onLoadingChanged: ((Bool) -> Void)?

    init(userId: String, apiClient: APIClient = .shared) {
        self.userId = userId
        self.apiClient = apiClient
    }

    func loadProfile() {
        onLoadingChanged?(true)
        apiClient.fetchUser(id: userId) { [weak self] result in
            DispatchQueue.main.async {
                self?.onLoadingChanged?(false)
                switch result {
                case .success(let user):
                    let profile = UserProfile(
                        displayName: user.name.uppercased(),
                        email: user.email.lowercased(),
                        avatarUrl: URL(string: user.avatarUrl)
                    )
                    self?.onProfileLoaded?(profile)
                case .failure(let error):
                    self?.onError?(error.localizedDescription)
                }
            }
        }
    }
}
```

### `UserProfileViewController.swift`

```swift
import UIKit

class UserProfileViewController: UIViewController {
    @IBOutlet weak var nameLabel: UILabel!
    @IBOutlet weak var emailLabel: UILabel!
    @IBOutlet weak var avatarImageView: UIImageView!
    @IBOutlet weak var loadingSpinner: UIActivityIndicatorView!

    var viewModel: UserProfileViewModel!

    override func viewDidLoad() {
        super.viewDidLoad()
        bindViewModel()
        viewModel.loadProfile()
    }

    private func bindViewModel() {
        viewModel.onProfileLoaded = { [weak self] profile in
            self?.nameLabel.text = profile.displayName
            self?.emailLabel.text = profile.email
            if let url = profile.avatarUrl {
                self?.loadAvatar(url)
            }
        }
        viewModel.onError = { [weak self] message in
            self?.showError(message)
        }
        viewModel.onLoadingChanged = { [weak self] isLoading in
            isLoading ? self?.loadingSpinner.startAnimating()
                      : self?.loadingSpinner.stopAnimating()
        }
    }

    private func loadAvatar(_ url: URL) { /* ... */ }
    private func showError(_ message: String) { /* ... */ }
}
```

## Verification

- `UserProfileViewModel` is testable without UIKit — inject a mock `APIClient`.
- Formatting logic is in the ViewModel, not the view.
- Adding a new data field requires no changes to the networking code.
- Navigation (alerts, segues) is handled by the Coordinator, not the VC.
- The ViewController is a thin binding layer — easy to review and maintain.
