import React from "react";

function Wrapper({ children }) {
    const style = {
        border : 'apx solid black',
        padding : '16px',
    };
    return <div style={style}>{ children }</div>;
}