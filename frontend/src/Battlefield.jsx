import { useState } from "react"

function Battlefield(props){
    const [hp, setHp] = useState(3)
    return (
        <>
            <h1>Battlefield</h1>

            <p>HP : {hp}</p>
            <button onClick={() => setHp(hp - 1)}>
                Hurt
            </button>
        </>
    )
}

export default Battlefield