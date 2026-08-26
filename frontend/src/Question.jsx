import { useState,useEffect } from "react"
import "./Question.css"

function Question(props) {

    const questionData = props.questionData
    const explanation = questionData.explanation
    const options = questionData.options

    const [selectedOptionId, setSelectedOptionId] = useState(null)
    const checkCount = props.checkCount
    const showDialog = props.showDialog
    const isWin = props.isWin
    const [showResult, setShowResult] = useState(false)

    useEffect(function () {
        setSelectedOptionId(null)
    }, [questionData.id])

    useEffect(()=> {
        if (showDialog === true){
            setTimeout(() => {
                setShowResult(true)
            }, 600)
        }
    }, [checkCount])

    return (
        <div className="question">
            <main className="question-main">
                <h2 className="question-type">
                    {questionData.questionType}
                </h2>

                <h2 className="question-description">
                    {questionData.description}
                </h2>

                <div className="question-options">
                    {options.map(function (option) {
                        return (
                            <h3 
                                className="option-description"
                                key={option.id}
                                >
                                {option.title} : {option.description}
                            </h3>
                        )
                    })}
                </div>
            </main>

            {showResult && (
                <div className="result-overlay">
                    <div className="result-dialog">
                        <p className="dialog-result">
                            {isWin === null
                                ? "Congratulations! You are correct!"
                                : isWin === true
                                    ? "You win!"
                                    : "You lose! Good luck next time!"
                            }
                        </p>
                        <p className="question-explanation">
                            {explanation}
                        </p>
                        <button
                            onClick={async () =>{
                                await props.processContinue()
                                setShowResult(false)
                            }}
                        >
                            Continue
                        </button>
                    </div>
                </div>
            )}

            <footer className="question-footer">
                <div className="answer-options">
                    {options.map(function (option) {
                        return (
                            <button 
                                type="button"
                                key={option.id}
                                disabled={questionData.removedOptionsId.includes(option.id)}
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
                            </button>
                        )
                    })}
                </div>

                <div className="check-options">

                    <button
                        type="button"
                        // disabled={selectedOptionId === null}
                        onClick={() => {
                            props.processSkill()
                        }}
                    >
                        Skill
                    </button>

                    <button
                        type="button"
                        disabled={selectedOptionId === null}
                        onClick={() => {
                            props.processCheck(selectedOptionId)
                        }}
                    >
                        Check
                    </button>

                    <button
                        type="button"
                        onClick={() => {
                            props.processQuit()
                        }}
                    >
                        Quit
                    </button>
                </div>
            </footer>
        </div>
    )
}

export default Question