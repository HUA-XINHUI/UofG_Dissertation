import { useState } from "react"

import Challenge from "./Challenge.jsx"
import Battlefield from "./Battlefield.jsx"

function App(props) {

    const [challengeData, setChallengeData] = useState(props.challengeData)
    const [questionData, setQuestionData] = useState(props.questionData)

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
        if (data.isEnd){
            window.location.href = data.redirectUrl
            return
        }
        setChallengeData(data.challengeData)
        setQuestionData(data.questionData)
    }

    // async function processContinue(){
    //     const formData = new FormData()
    //     formData.append("action", "continue")
    //     const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value
    //     formData.append("csrfmiddlewaretoken", csrfToken)
    //     const response = await fetch(
    //         window.location.href,
    //         {
    //             method : "POST",
    //             body : formData,
    //         }
    //     )
    //     const data = await response.json()
    //     console.log(data)
    //     setQuestion(data.questionData)
    //     setSelectedOptionId(null)
    // }

    return (
        <>
            <Challenge
                challengeData={questionData}
            />
            <Battlefield
                questionData={challengeData}
            />
        </>
    )
}