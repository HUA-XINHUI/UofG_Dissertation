import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'

import Battlefield from './Battlefield.jsx'

const battlefieldRoot = document.querySelector("#battlefield-root")

if (battlefieldRoot) {

  const playerName = battlefieldRoot.dataset.playerName
  const currentHp = battlefieldRoot.dataset.currentHp

  createRoot(battlefieldRoot).render(
    <Battlefield 
      playerName={playerName}
      currentHp={currentHp}
    />
  )
}
