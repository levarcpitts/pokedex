import React from 'react'
import './Header.css'
import pokedex_title from './/images/Pokedex.png'

function Header() {
  return (
    <div className="red-background">
      <div className="logo">
        <img src={pokedex_title} alt="Logo" className="header-image" />
        </div>
        <div className="search-bar">
        <input
            type="text"
            placeholder="Search..." 
        />
        </div>
    </div>
  )
}

export default Header