import { useState, useEffect } from "react"
import "./Battlefield.css"

function Battlefield(props) {

    const [currentHp, setCurrentHp] = useState(props.currentHp)
    const [currentMp, setCurrentMp] = useState(props.currentMp)

    const [playerState, setPlayerState] = useState("idle")
    const [enemyState, setEnemyState] = useState("idle")

    const [result, setResult] = useState(null)
    const [explanation, setExplanation] = useState("")
    const [showResult, setShowResult] = useState(false)

    function correct(){
        setPlayerState("attack")
        setTimeout(function () {
            setEnemyState("hurt")
        }, 200)
        setTimeout(function () {
            setEnemyState("idle")
        }, 400)
        setTimeout(function () {
            setPlayerState("idle")
        }, 500)
    }

    function wrong(){
        setEnemyState("attack")
        setTimeout(function () {
            setPlayerState("hurt")
        }, 200)
        setTimeout(function () {
            setPlayerState("idle")
        }, 400)
        setTimeout(function () {
            setEnemyState("idle")
        }, 500)
    }

    useEffect(function () {
        function handleChallengeResult(event) {
            const data = event.detail
            console.log("Battlefield received:", data)
            setCurrentHp(data.current_hp)
            setCurrentMp(data.current_mp)
            setResult(data.result)
            setExplanation(data.explanation)
            if (data.result === "correct") {
                correct()
            }
            if (data.result === "wrong") {
                wrong()
            }
            setTimeout(function () {
                setShowResult(true)
            }, 550)
        }
        window.addEventListener(
            "challenge-result",
            handleChallengeResult
        )
        return function () {
            window.removeEventListener(
                "challenge-result",
                handleChallengeResult
            )
        }
    }, [])

    return (
        <div className="battlefield">

            <div>
                <p>{props.playerName}</p>
                <p>HP: {currentHp}</p>
                <p>MP: {currentMp}</p>
            </div>

            <div
                className={`player player-${playerState}`}
            >
                Player
            </div>

            <div
                className={`enemy enemy-${enemyState}`}
            >
                Slime
            </div>

            {showResult && (
                <div className="result-dialog">

                    <h2>
                        {result === "correct"
                            ? "Correct!"
                            : "Wrong!"
                        }
                    </h2>

                    <p>
                        {explanation}
                    </p>

                    <button>
                        Continue
                    </button>

                </div>
            )}

        </div>
    )
}

export default Battlefield