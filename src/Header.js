import React from 'react'
import './Header.css'
import pokedex_title from './/images/Pokedex.png'

function Header() {
  return (
    <div className="red-background">
        <img src={pokedex_title} alt="Logo" className="header-image" />
    </div>
  )
}

export default Header