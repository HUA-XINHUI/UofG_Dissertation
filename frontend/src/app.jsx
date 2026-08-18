import { useState } from "react"

import Challenge from "./Challenge.jsx"
import Question from "./Question.jsx"

function App(props) {

    const [isCorrect, setIsCorrect] = useState(null)
    const [challengeData, setChallengeData] = useState(props.challengeData)
    const [questionData, setQuestionData] = useState(props.questionData)
    const [checkCount, setCheckCount] = useState(1)

    async function processCheck(selectedOptionId){
        const formData = new FormData()
        formData.append("action", "check")
        formData.append("selected_option", selectedOptionId)
        const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value
        formData.append("csrfmiddlewaretoken", csrfToken)
        const response = await fetch(
            window.location.href,
            {
                method : "POST",
                body : formData,
            }
        )
        const data = await response.json()
        setIsCorrect(data.isCorrect)
        setChallengeData(data.challengeData)
        setCheckCount( checkCount + 1)
    }

    async function processContinue(){
        const formData = new FormData()
        formData.append("action", "continue")
        const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value
        formData.append("csrfmiddlewaretoken", csrfToken)
        const response = await fetch(
            window.location.href,
            {
                method : "POST",
                body : formData,
            }
        )
        const data = await response.json()
        if (data.isEnd){
            window.location.href = data.redirectUrl
            return
        }
        setQuestionData(data.questionData)
    }

    async function processSkill(){
        const formData = new FormData()
        formData.append("action", "skill")
        const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value
        formData.append("csrfmiddlewaretoken", csrfToken)
        const response = await fetch(
            window.location.href,
            {
                method : "POST",
                body : formData,
            }
        )
        const data = await response.json()

        setChallengeData((oldData) => { 
            return { ...oldData, ...data.challengeData, } 
        }) 

        setQuestionData((oldData) => {
            return { ...oldData, ...data.questionData}
        })
    }

    async function processQuit(){
        const formData = new FormData()
        formData.append("action", "quit")
        const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value
        formData.append("csrfmiddlewaretoken", csrfToken)
        const response = await fetch(
            window.location.href,
            {
                method : "POST",
                body : formData,
            }
        )
        const data = await response.json()
        window.location.href = data.redirectUrl
    }

    return (
        <>
            <Challenge
                isCorrect={isCorrect}
                checkCount={checkCount}
                challengeData={challengeData}
                processContinue={processContinue}
            />

            <Question
                questionData={questionData}
                processCheck={processCheck}
                processSkill={processSkill}
                processQuit={processQuit}
            />
        </>
    )
}

export default App