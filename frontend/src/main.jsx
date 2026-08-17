// import { StrictMode } from 'react'
// import { createRoot } from 'react-dom/client'

// import Challenge from './Challenge.jsx'

// const challengeRoot = document.querySelector("#challenge-root")
// if (challengeRoot) {

//     const challengeData = JSON.parse(document.querySelector("#challenge-data").textContent)
//     const questionData = JSON.parse(document.querySelector("#question-data").textContent)

//     createRoot(challengeRoot).render(
//         <Challenge
//             challengeData={challengeData}
//             questionData={questionData}
//         />
//     )
// }

// const challengeForm = document.querySelector("#challenge-form")
// if (challengeForm) {
//     challengeForm.addEventListener("submit", async function (event) {
//         const submitButton = event.submitter
//         if (submitButton.value !== "check") {
//             return
//         }
//         event.preventDefault()
//         const formData = new FormData(challengeForm)
//         formData.append(
//             submitButton.name,
//             submitButton.value
//         )
//         const response = await fetch(
//             window.location.href,
//             {
//                 method: "POST",
//                 body: formData,
//             }
//         )
//         const data = await response.json()
//         console.log(data)
//         window.dispatchEvent(
//           new CustomEvent("challenge-result", {
//             detail: data
//           })
// )
//     })
// }

import { StrictMode } from "react"
import { createRoot } from "react-dom/client"
import App from "./App.jsx"

const root = document.querySelector("#challenge-root")

createRoot(root).render(
    <StrictMode>
        <App 
            challengeData={root.dataset.challengeData}
            questionData={root.dataset.questionData}
        />
    </StrictMode>
)