import { useState, useEffect } from "react"
import "./Challenge.css"

function Challenge(props) {

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
        }
        if (isCorrect === false) {
            wrong()
        }
    }, [checkCount])

    return (
        <div className="battlefield">

            <header className="battlefield-header">
                <div className="player-information-zone">
                    <p>HP: {currentHp}</p>
                    <p>MP: {currentMp}</p>
                </div>
                <div className="enemy-information-zone">
                    <p>BOSS: {bossCurrentHp} / {bossMaxHp}</p>
                </div>
            </header>

            <div className="combat-zone">
                <div className={`player player-${playerState}`}>
                    <div className="character-image">
                        Player Image
                    </div>
                    <div className="player-name">
                        {challengeData.playerAlias}
                    </div>
                </div>

                <div className={`enemy enemy-${enemyState}`}>
                    <div className="enemy-image">
                        Enemy Image
                    </div>
                    <div className="enemy-name">
                        {challengeData.bossName}
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Challenge


