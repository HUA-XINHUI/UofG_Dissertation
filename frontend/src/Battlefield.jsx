import { useState } from "react"
import "./Battlefield.css"

function Battlefield(props) {

    const [currentHp, setCurrentHp] = useState(props.currentHp)

    const [isAttacking, setIsAttacking] = useState(false)
    const [isEnemyHurt, setIsEnemyHurt] = useState(false)

    function attack() {

        // 1. 玩家开始攻击
        setIsAttacking(true)

        // 2. 200ms 后敌人受伤
        setTimeout(function () {
            setIsEnemyHurt(true)
        }, 200)

        // 3. 400ms 后敌人恢复
        setTimeout(function () {
            setIsEnemyHurt(false)
        }, 400)

        // 4. 500ms 后玩家回原位
        setTimeout(function () {
            setIsAttacking(false)
        }, 500)
    }

    return (
        <div className="battlefield">

            <div
                className={
                    isAttacking
                        ? "player player-attacking"
                        : "player"
                }
            >
                <p>{props.playerName}</p>
                <p>HP: {currentHp}</p>
            </div>

            <div
                className={
                    isEnemyHurt
                        ? "enemy enemy-hurt"
                        : "enemy"
                }
            >
                Slime
            </div>

            <button onClick={attack}>
                Attack
            </button>

        </div>
    )
}

export default Battlefield