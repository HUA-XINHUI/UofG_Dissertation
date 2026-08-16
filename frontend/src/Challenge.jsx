import { useState } from "react"

import Battlefield from "./Battlefield.jsx"

function Challenge(props) {

    const [question, setQuestion] = useState(props.questionData)
    const [selectedOptionId, setSelectedOptionId] = useState(null)

    async function processCheck(){
        const formData = new FormData()
        formData.append("selected_option", selectedOptionId)
        formData.append("action", "check")
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
        console.log(data)
        window.dispatchEvent(
            new CustomEvent("challenge-result", {
                detail: data
            })
        )
    }

    return (
        <div className="challenge">
            <Battlefield
                playerName={props.playerName}
                currentHp={props.currentHp}
                currentMp={props.currentMp}
            />
            <div className="question">
                <h2> {question.title} </h2>
                <p> {question.description} </p>
                <div className="options">
                    {question.options.map(function (option) {
                        return (
                            <button 
                                key={option.id}
                                className={
                                    selectedOptionId === option.id
                                        ? "answer-option selected"
                                        : "answer-option"
                                }
                                onClick={
                                    function(){
                                        setSelectedOptionId(option.id)
                                }
                            }
                            >
                                <strong> {option.title} </strong>
                                <span> {option.description} </span>
                            </button>
                        )
                    })}
                    <button
                        className="check-button"
                        disabled={selectedOptionId === null}
                        onClick={processCheck}
                    >
                        Check
                    </button>
                </div>
            </div>
        </div>
    )
}

export default Challenge