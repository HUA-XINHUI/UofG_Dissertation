import { useState, useEffect } from "react"
import "./Challenge.css"

import CharacterSprite from "./sprites/CharacterSprite"

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
        setTimeout(() => {
            if (bossCurrentHp <= 0) {
                setEnemyState("die")
            } else {
                setEnemyState("hurt")
            }
        }, 400)
    }

    function wrong(){
        setEnemyState("attack")
        setTimeout(() => {
            if (currentHp <= 0) {
                setPlayerState("die")
            } else {
                setPlayerState("hurt")
            }
        }, 400)
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
                    <p>{ challengeData.characterClass }</p>
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
                        <CharacterSprite
                            character={challengeData.characterAssetKey}
                            state={playerState}
                            facing="right"
                            onAnimationEnd={() => {
                                if (playerState !== "die") {
                                    setPlayerState("idle")
                                }
                            }}
                        />
                    </div>
                    <div className="player-name">
                        {challengeData.playerAlias}
                    </div>
                </div>

                <div className={`enemy enemy-${enemyState}`}>
                    <div className="enemy-image">
                        <CharacterSprite
                            character={challengeData.enemyAssetKey}
                            state={enemyState}
                            facing="left"
                            onAnimationEnd={() => {
                                if (enemyState !== "die") {
                                    setEnemyState("idle")
                                }
                            }}
                        />
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


