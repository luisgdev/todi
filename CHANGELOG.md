# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [0.0.3] - 2023-03-06

### Added
- New feature: Import and Export todi databases.
    - Import from anywhere, by indicating the path of the backup file.
    - Backup files are exported to `~/todi_backups/` directory. 

### Fixed
- Missing docstrings.
- Removed docstrings from help messages.

### Changed
- Database directory is now `~/.todi/`. 


## [0.0.2] - 2022-09-20

### Added
- CHANGELOG file.

### Fixed
- `Todi` has being creating the db directory on every directory it was being called from. Causing that sometimes, there was ***no pending tasks***.
    - From now on, the database directory will be created on `home/`.
- Type hint errors detected by `mypy`.

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
