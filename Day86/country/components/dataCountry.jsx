import React from "react";

export function DataCountry({ data }){
    if (!('Error' == data)){
        return (
            <ul>
                {data.map((todo) => (
                    <li>{todo['name']} - {todo['alpha3Code']} - {todo['capital']}</li>
                ))}
            </ul>
        )
    } else{
        return (
            <ul>
                <li>Country not found</li>
            </ul>
        )
    }
}

export function SearchMatchCountry({ data }) {
    if (!('Error' == data)){
        return (
            <ul>
                {data.map((todo) => (
                    <li>{todo['name']} - {todo['alpha3Code']} - {todo['capital']}</li>
                ))}
            </ul>
        )
    } else{
        return (
            <ul>
                <li>Country not found</li>
            </ul>
        )
    }
}

export function SearchInAllCountrys({ data, filter }) {
    // data[0].filter(name => data[0]['name'].toUpperCase().includes(filter.toUpperCase()))
    if (!('Error' == data)){
        return (
            <ul>
                {data[0].map((todo) => (
                    <li>{todo['name']}</li>
                ))}
            </ul>
        )
    } else{
        return (
            <ul>
                <li>Country not found</li>
            </ul>
        )
    }
}