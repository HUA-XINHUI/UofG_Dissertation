import { StrictMode } from "react"
import { createRoot } from "react-dom/client"
import App from "./app.jsx"

const root = document.querySelector("#challenge-root")

const challengeDataElement = document.querySelector("#challenge-data")
const questionDataElement = document.querySelector("#question-data")

const challengeData = JSON.parse(challengeDataElement.textContent)
const questionData = JSON.parse(questionDataElement.textContent)

createRoot(root).render(
    <StrictMode>
        <App
            challengeData={challengeData}
            questionData={questionData}
        />
    </StrictMode>
)