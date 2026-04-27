// Before: Callback hell — nested callbacks make error handling and
// control flow difficult to follow.

function loadUserProfile(userId) {
  getUser(userId, function (err, user) {
    if (err) {
      console.error("Failed to load user:", err);
      return;
    }

    getPosts(user.id, function (err, posts) {
      if (err) {
        console.error("Failed to load posts:", err);
        return;
      }

      getComments(posts[0].id, function (err, comments) {
        if (err) {
          console.error("Failed to load comments:", err);
          return;
        }

        getLikes(comments[0].id, function (err, likes) {
          if (err) {
            console.error("Failed to load likes:", err);
            return;
          }

          renderProfile(user, posts, comments, likes);
        });
      });
    });
  });
}
