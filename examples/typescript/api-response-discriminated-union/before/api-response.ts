// Before: Using `any` types loses type safety and makes refactoring dangerous.

interface ApiResponse {
  status: number;
  data: any;       // Could be anything
  error?: any;     // Could be anything
}

function handleResponse(response: ApiResponse): string {
  if (response.status >= 400) {
    return `Error: ${response.error?.message ?? "Unknown"}`;
  }

  // No type information — we have to guess the shape
  const user = response.data;
  return `Hello, ${user.first_name} ${user.last_name}!`;
}

// Caller has no idea what shape `data` should be
const resp: ApiResponse = {
  status: 200,
  data: { first_name: "John", last_name: "Doe" },
};
console.log(handleResponse(resp));
