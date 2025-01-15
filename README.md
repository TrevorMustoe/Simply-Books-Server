Simply Books Server
The Simply Books API provides a streamlined way to manage books and authors with CRUD functionality, user-specific data access, and Firebase authentication.

Features
Books: Add, update, and delete books, including their titles, authors, prices, sale status, and descriptions.
Authors: Manage authors with their personal details and favorite status.
Genres: Categorize books by genres and manage them.
User Authentication: Books and authors are linked to the authenticated user's UID, ensuring user-specific data access.
Endpoints
Books
GET /book
Retrieve a list of all books.
Response: JSON array of book objects.

GET /book/:id
Retrieve the details of a specific book by its ID.
Response: JSON object containing book details.

GET /book?uid={uid}
Retrieve books based on a specific user's UID.
Response: JSON array of books linked to the provided UID.

POST /book
Create a new book.
Request body: JSON object containing book details (author ID, title, price, description, etc.).

PUT /book/:id
Update an existing book by its ID.
Request body: JSON object containing updated book details.

DELETE /book/:id
Delete a book by its ID.
Response: HTTP 204 No Content on successful deletion.

Authors
GET /author
Retrieve a list of all authors.
Response: JSON array of author objects.

GET /author/:id
Retrieve the details of a specific author by their ID.
Response: JSON object containing author details.

GET /author?uid={uid}
Retrieve authors based on a specific user's UID.
Response: JSON array of authors linked to the provided UID.

POST /author
Create a new author.
Request body: JSON object containing author details (email, first name, last name, etc.).

PUT /author/:id
Update an existing author's details by their ID.
Request body: JSON object containing updated author details.

DELETE /author/:id
Delete an author by their ID.
Response: HTTP 204 No Content on successful deletion.

Genres
GET /genre
Retrieve a list of all genres.
Response: JSON array of genre objects.

GET /genre/:id
Retrieve the details of a specific genre by its ID.
Response: JSON object containing genre details.

POST /genre
Create a new genre.
Request body: JSON object containing genre details.

PUT /genre/:id
Update an existing genre by its ID.
Request body: JSON object containing updated genre details.

DELETE /genre/:id
Delete a genre by its ID.
Response: HTTP 204 No Content on successful deletion.

Genre-Book
GET /genre_book
Retrieve a list of books categorized by genre.
Response: JSON array of books grouped by genre.

GET /genre_book/:id
Retrieve books within a specific genre by genre ID.
Response: JSON array of books within the requested genre.
