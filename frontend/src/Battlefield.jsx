import { useState } from "react"
import "./Battlefield.css"

function Battlefield(props) {

    const [currentHp, setCurrentHp] = useState(props.currentHp)
    const [currentMp, setCurrentMp] = useState(props.currentMp)

    const [playerState, setPlayerState] = useState("idle")
    const [enemyState, setEnemyState] = useState("idle")

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

            <button onClick={correct}>
                Correct
            </button>

            <button onClick={wrong}>
                Wrong
            </button>
        </div>
    )
}

export default Battlefield