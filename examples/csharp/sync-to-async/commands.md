# Commands

## Run Original Code

```bash
# Compile and run the synchronous version
csc before/UserService.cs -out:before/UserService.exe
mono before/UserService.exe
# or on .NET Core:
dotnet run --project before/
```

## Run Refactored Code

```bash
# Compile and run the async version
csc after/*.cs -out:after/UserService.exe
mono after/UserService.exe
```

## Run Tests

```bash
dotnet test tests/
```

## Validate Behavior Preservation

The refactoring changes `FetchUserData` from synchronous blocking (`Task.Result`) to proper async/await. The public API changes from `string FetchUserData(string)` to `Task<string> FetchUserDataAsync(string)`.

Validation Level: **Static reasoning only** — requires a real HTTP endpoint to run end-to-end.
