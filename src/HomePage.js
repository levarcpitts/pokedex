import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './HomePage.css';  

function HomePage() {
  const [pokemon, setPokemon] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(0);
  const itemsPerPage = 8;

  useEffect(() => {
    const fetchPokemon = async () => {
      const offset = (currentPage - 1) * itemsPerPage;
      const response = await axios.get(`http://127.0.0.1:5000/api/pokemon?limit=${itemsPerPage}&offset=${offset}`);
      
      setPokemon(response.data.results);
      setTotalPages(Math.ceil(response.data.count / itemsPerPage));
    };

    fetchPokemon();
  }, [currentPage]);

  const handlePreviousPage = () => {
    if (currentPage > 1) {
      setCurrentPage(currentPage - 1);
    }
  };

  const handleNextPage = () => {
    if (currentPage < totalPages) {
      setCurrentPage(currentPage + 1);
    }
  };

  return (
    <div className="homepage">
      <div className="pokemon-grid">
        {pokemon.map((poke, index) => (
          <div className="pokemon-card" key={index}>
            <img src={poke.image} alt={poke.name} className="pokemon-image" />
            <div className="pokemon-info">
              <div className="pokemon-types">
                {poke.types.map((type, typeIndex) => (
                  <span className="pokemon-type" key={typeIndex}>{type}</span>
                ))}
              </div>
              <div className="pokemon-name-number">
                <strong className="pokemon-name">{poke.name}</strong>
                <span className="pokemon-number">{poke.number}</span>
              </div>
            </div>
          </div>
        ))}
      </div>
      <div className="pagination">
        <button onClick={handlePreviousPage} disabled={currentPage === 1}>
          Previous
        </button>
        <span>Page {currentPage} of {totalPages}</span>
        <button onClick={handleNextPage} disabled={currentPage === totalPages}>
          Next
        </button>
      </div>
    </div>
  );
}

export default HomePage;