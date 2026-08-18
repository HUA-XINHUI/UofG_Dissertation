import { useState,useEffect } from "react"

function Question(props) {
    console.log(props.questionData)
    const questionData = props.questionData
    const title = questionData.title
    const description = questionData.description
    const explanation = questionData.explanation
    const options = questionData.options

    const [selectedOptionId, setSelectedOptionId] = useState(null)

    useEffect(function () {
        setSelectedOptionId(null)
    }, [questionData.id])

    return (
        <>
            <h1>{title}</h1>
            <h1>{description}</h1>
            <h1>{explanation}</h1>
            {options.map(function (option) {
                return (
                    <button 
                        type="button"
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
                type="button"
                // disabled={selectedOptionId === null}
                onClick={() => {
                    props.processSkill()
                }}
            >
                skill
            </button>

            <button
                type="button"
                disabled={selectedOptionId === null}
                onClick={() => {
                    props.processCheck(selectedOptionId)
                    console.log(selectedOptionId)
                }}
            >
                check
            </button>

            <button
                type="button"
                onClick={() => {
                    props.processQuit()
                }}
            >
                quit
            </button>
        </>
    )
}

export default Question