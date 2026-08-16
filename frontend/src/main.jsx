import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'

import Challenge from './Challenge.jsx'

const challengeRoot = document.querySelector("#challenge-root")

if (challengeRoot) {

    const playerName = challengeRoot.dataset.playerName
    const currentHp = Number(challengeRoot.dataset.currentHp)
    const currentMp = Number(challengeRoot.dataset.currentMp)

    const questionDataElement = document.querySelector("#question-data")
    const questionData = JSON.parse(questionDataElement.textContent)

    console.log("questionDataElement:", questionDataElement)
    console.log("raw text:", questionDataElement.textContent)
    console.log("questionData:", questionData)
    
    createRoot(challengeRoot).render(
        <Challenge
            playerName={playerName}
            currentHp={currentHp}
            currentMp={currentMp}
            questionData={questionData}
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
