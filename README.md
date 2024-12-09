# user_management

## Funkcje:

- ### Funkcja `add_user(user_data)`
- Funkcja, która dodaje nowego użytkownika do pliku `users.json`.

- ### Funkcja `edit_user(user_id, updated_data)`
- Funkcja do edycji danych istniejącego użytkownika.

- ### Funkcja `remove_user(user_id)`
- Funkcja do usuwania użytkownika na podstawie jego identyfikatora.

- #### Funkcja `load_users()`
- Funkcja do odczytu istniejących użytkowników z pliku `users.json`.

- ### Funkcja `validate_nip(nip)`
- Walidacja numeru NIP

- ### Funkcja `validate_pesel(pesel)`
- Walidacja numeru PESEL.

- ### Funkcja `validate_regon(regon)`
- Walidacja numeru REGON.

- ### Funkcja `generate_password()`
- Funkcja generującą silne hasło o długości 12 znaków,

- ### Funkcja `validate_password(password)`
- Funkcja walidującą czy hasło spełnia minimalne wymagania (długość, złożoność)
