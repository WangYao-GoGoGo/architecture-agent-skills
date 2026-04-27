# Monolithic Component → Decomposed Components

Refactored from a single monolithic component into focused, reusable components with a custom hook for data fetching.

## Design Pressure

- `ProductPage` handled data fetching, filtering, sorting, pagination, and rendering.
- State variables were scattered — resetting `page` on filter change was manual.
- The component was not reusable — any page needing a product list would duplicate this logic.
- Testing required rendering the entire page.

## Applied Pattern

**Component decomposition + custom hooks** — extract data fetching into `useProducts` hook. Split UI into `SearchBar`, `ProductFilters`, `ProductList`, and `Pagination` components.

## After Code

### `useProducts.js` — Custom hook

```javascript
import { useState, useEffect } from 'react';

function useProducts({ search, category, sortBy, page, pageSize }) {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    fetch(`/api/products?search=${search}&category=${category}&sort=${sortBy}&page=${page}&pageSize=${pageSize}`)
      .then(res => {
        if (!res.ok) throw new Error('Failed to fetch');
        return res.json();
      })
      .then(data => {
        if (!cancelled) {
          setProducts(data);
          setLoading(false);
        }
      })
      .catch(err => {
        if (!cancelled) {
          setError(err.message);
          setLoading(false);
        }
      });
    return () => { cancelled = true; };
  }, [search, category, sortBy, page, pageSize]);

  return { products, loading, error };
}
```

### `ProductPage.js` — Composed from small components

```javascript
function ProductPage() {
  const [filters, setFilters] = useState({ search: '', category: 'all', sortBy: 'name' });
  const [page, setPage] = useState(1);
  const { products, loading, error } = useProducts({ ...filters, page, pageSize: 10 });

  const handleFilterChange = (key, value) => {
    setFilters(f => ({ ...f, [key]: value }));
    setPage(1);
  };

  if (loading) return <LoadingSpinner />;
  if (error) return <ErrorMessage message={error} />;

  return (
    <div>
      <h1>Products</h1>
      <SearchBar value={filters.search} onChange={v => handleFilterChange('search', v)} />
      <ProductFilters
        category={filters.category}
        sortBy={filters.sortBy}
        onCategoryChange={v => handleFilterChange('category', v)}
        onSortChange={v => handleFilterChange('sortBy', v)}
      />
      <ProductList products={products} />
      <Pagination page={page} onPageChange={setPage} />
    </div>
  );
}
```

## Verification

- Same UI and behavior for the same inputs.
- `useProducts` hook is testable without rendering components.
- Each component (`SearchBar`, `ProductFilters`, `ProductList`, `Pagination`) is independently reusable.
- Adding a new filter requires no changes to the data fetching logic.
- Race conditions are handled via the `cancelled` flag in the hook.
