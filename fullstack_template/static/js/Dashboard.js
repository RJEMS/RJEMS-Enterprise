import React from "react"

export default class Dashboard extends React.Component {


 render() {
        return (
            <div>
                <button> Enabled Button</button> &nbsp;
                <button disabled={true}>Disabled Button </button>
            </div>
        )
    }
}