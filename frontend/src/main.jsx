import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'

import Battlefield from './Battlefield.jsx'

const battlefieldRoot = document.querySelector("#battlefield-root")
if (battlefieldRoot) {

  const playerName = battlefieldRoot.dataset.playerName
  const currentHp = battlefieldRoot.dataset.currentHp
  const currentMp = battlefieldRoot.dataset.currentMp

  createRoot(battlefieldRoot).render(
    <Battlefield 
      playerName={playerName}
      currentHp={currentHp}
      currentMp={currentMp}
    />
  )
}

const challengeForm = document.querySelector("#challenge-form")
if (challengeForm) {
    challengeForm.addEventListener("submit", async function (event) {
        const submitButton = event.submitter
        if (submitButton.value !== "check") {
            return
        }
        event.preventDefault()
        const formData = new FormData(challengeForm)
        formData.append(
            submitButton.name,
            submitButton.value
        )
        const response = await fetch(
            window.location.href,
            {
                method: "POST",
                body: formData,
            }
        )
        const data = await response.json()
        console.log(data)
        window.dispatchEvent(
          new CustomEvent("challenge-result", {
            detail: data
          })
)
    })
}
