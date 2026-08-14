import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

import Battlefield from "./Battlefield"

function App() {
  return (
    <>
      <Battlefield 
        playerName="Warrior"
        enemyName="slime"
      />
    </>
  )
}

export default App
