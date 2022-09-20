# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [0.0.2] - 2022-09-20

### Added
- This CHANGELOG file.

### Changed
- Database directory was modified to keep it hidden and identified.
    - Created a new directory `.todi/`, to storage the database.
    - The old directory `db/`, will not be deleted or modified.
    - The database will be moved from `db/` to `.todi/`.

## [0.0.1] - 2022-09-17

### Created
- **Todi**, a command line tool to manage to-do tasks.
    - `List`, `Add`, `Update` and `Delete` tasks.
    - Change status: `TODO` (default), `DOING` and `DONE`.
    - `Clean` command to remove `DONE` tasks.
