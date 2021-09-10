import React from "react";

export function DataCountry({ data }){
    return (
        <ul>
            {data.map((todo) => (
                <li>{todo['name']} - {todo['alpha3Code']} - {todo['capital']}</li>
            ))}
        </ul>
    )
}