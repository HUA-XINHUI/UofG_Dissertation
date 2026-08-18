import { useState, useEffect } from "react"
import Question from "./Question.jsx"
import "./Challenge.css"

function Challenge(props) {

    console.log(props)
    // console.log(props.challengeData.bossCurrentHp)

    const challengeData = props.challengeData
    const isCorrect = props.isCorrect
    const characterId = challengeData.characterId
    const currentHp = challengeData.currentHp
    const currentMp = challengeData.currentMp
    const buffs = challengeData.buffs
    const bossMaxHp = challengeData.bossMaxHp
    const bossCurrentHp = challengeData.bossCurrentHp

    const checkCount = props.checkCount
    const [playerState, setPlayerState] = useState("idle")
    const [enemyState, setEnemyState] = useState("idle")
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

    useEffect(()=> {
        if (isCorrect === true) {
            correct()
            setTimeout(() => {
                setShowResult(true)
            }, 550)
        }
        if (isCorrect === false) {
            wrong()
        }
    }, [checkCount])

    return (
        <div className="battlefield">
            <div>
                <p>HP: {currentHp}</p>
                <p>MP: {currentMp}</p>
            </div>
            <div
                className={`player player-${playerState}`}
            >
                Player
            </div>
            <div>
                <p>BOSS: {bossCurrentHp} / {bossMaxHp}</p>
            </div>
            <div
                className={`enemy enemy-${enemyState}`}
            >
                Slime
            </div>

            {showResult && (
                <div className="result-dialog">
                    <button
                        onClick={async () =>{
                            await props.processContinue()
                            setShowResult(false)
                        }}>
                        Continue
                    </button>
                </div>
            )}

        </div>
    )
}

export default Challenge


