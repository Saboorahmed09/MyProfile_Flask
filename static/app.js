document.addEventListener("DOMContentLoaded", function () {
    const postForm = document.getElementById("post-form");

    if (postForm) {
        postForm.addEventListener("submit", function (event) {
            event.preventDefault();

            const formData = new FormData(postForm);

            fetch("/", {
                method: "POST",
                body: formData,
            })
                .then(response => response.json())
                .then(data => {
                    console.log("Response from server:", data);

                    // Append the new post to the profile container
                    appendPost(data);
                })
                .catch(error => console.error("Error:", error));
        });
    }

    function appendPost(post) {
        const profileContainer = document.getElementById("profile-container");

        if (profileContainer) {
            console.log("Appending new post:", post);

            const card = document.createElement("div");
            card.classList.add("card", "mb-3");

            const cardBody = document.createElement("div");
            cardBody.classList.add("card-body");

            const cardTitle = document.createElement("h5");
            cardTitle.classList.add("card-title");
            cardTitle.textContent = post.title;

            const cardText = document.createElement("p");
            cardText.classList.add("card-text");
            cardText.textContent = post.content;

            cardBody.appendChild(cardTitle);
            cardBody.appendChild(cardText);
            card.appendChild(cardBody);

            // Insert the new card at the beginning of the container
            profileContainer.insertBefore(card, profileContainer.firstChild);
        }
    }
});
