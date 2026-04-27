// Before: A monolithic React component that handles data fetching,
// filtering, rendering, and pagination all in one file.

import React, { useState, useEffect } from 'react';

function ProductPage() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [search, setSearch] = useState('');
  const [category, setCategory] = useState('all');
  const [sortBy, setSortBy] = useState('name');
  const [page, setPage] = useState(1);
  const pageSize = 10;

  useEffect(() => {
    setLoading(true);
    fetch(`/api/products?search=${search}&category=${category}&sort=${sortBy}&page=${page}&pageSize=${pageSize}`)
      .then(res => {
        if (!res.ok) throw new Error('Failed to fetch');
        return res.json();
      })
      .then(data => {
        setProducts(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, [search, category, sortBy, page]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h1>Products</h1>
      <input
        placeholder="Search..."
        value={search}
        onChange={e => { setSearch(e.target.value); setPage(1); }}
      />
      <select value={category} onChange={e => { setCategory(e.target.value); setPage(1); }}>
        <option value="all">All</option>
        <option value="electronics">Electronics</option>
        <option value="clothing">Clothing</option>
      </select>
      <select value={sortBy} onChange={e => { setSortBy(e.target.value); setPage(1); }}>
        <option value="name">Name</option>
        <option value="price">Price</option>
      </select>
      <ul>
        {products.map(p => (
          <li key={p.id}>
            <h3>{p.name}</h3>
            <p>${p.price}</p>
          </li>
        ))}
      </ul>
      <button disabled={page === 1} onClick={() => setPage(p => p - 1)}>Previous</button>
      <span>Page {page}</span>
      <button onClick={() => setPage(p => p + 1)}>Next</button>
    </div>
  );
}
