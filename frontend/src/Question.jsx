import { useState,useEffect } from "react"

function Question(props) {

    const questionData = props.questionData
    const title = questionData.title
    const description = questionData.description
    const explanation = questionData.explanation
    const options = questionData.options

    const [selectedOptionId, setSelectedOptionId] = useState(null)
    const checkCount = props.checkCount
    const showDialog = props.showDialog
    const isEnd = props.isEnd
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
                <h2 className="question-description">
                    {description}
                </h2>
                {options.map(function (option) {
                    return (
                        <h2 key={option.id}>
                            {option.title} : {option.description}
                        </h2>
                    )
                })}
            </main>

            {showResult && (
                <div className="result-overlay">
                    <div className="result-dialog">
                        <p>
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
                            }}>
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
                        skill
                    </button>

                    <button
                        type="button"
                        disabled={selectedOptionId === null}
                        onClick={() => {
                            props.processCheck(selectedOptionId)
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
                </div>
            </footer>
        </div>
    )
}

export default Question