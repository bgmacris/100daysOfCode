import React, { Fragment, useState, useRef } from 'react';
import { DataCountry } from './components/dataCountry';
const request = require('request');

export function GetData(country) {
    const [data, setData] = useState([]);

    const CountryName = useRef();

    const SearchCountry = () => {
        const name = CountryName.current.value;
        if (name == '') return;
        let url = `https://restcountries.eu/rest/v2/name/${name}`
        request({
            url: url,
            json: true
        }, (error, response, body) => {
            setData((prevData) => {
                return [body[0]]
            });
        })
        CountryName.current.value = null;
    };

    return(
        <Fragment>
            <input ref={CountryName} type="text" placeholder="Search Country"></input>
            <button onClick={SearchCountry}>Search</button>
            <DataCountry data={data} />
        </Fragment>
    )
}