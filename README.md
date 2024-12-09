# user_management

## Nazwy funkcji:
- `add_user(user_data)`: Dodaje nowego użytkownika.
- `remove_user(user_id)`: Usuwa istniejącego użytkownika.
- `edit_user(user_id, updated_data)`: Edytuje dane użytkownika.
- `validate_nip(nip)`: Waliduje numer NIP.
- `validate_pesel(pesel)`: Waliduje numer PESEL.
- `validate_regon(regon)`: Waliduje numer REGON.
- `generate_password()`: Generuje silne hasło.
- `validate_password(password)`: Waliduje siłę hasła.

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
