import React, { useState, useRef  } from 'react';
import { DataCountry, SearchMatchCountry, SearchInAllCountrys } from './components/dataCountry';
import {
    BrowserRouter as Router,
    Route,
    Switch,
    Link
} from "react-router-dom";

const request = require('request');

export function GetData() {
    const getAllCountrys = () => {
        let countrys = [];
        request({
            url: `https://restcountries.eu/rest/v2/all`,
            json: true
        }, (error, response, body) => {
            if (!(404 === body['status'])){
                for (var i in body){
                    countrys.push(body[i])
                }
            }else{
                body = 'Error'
                countrys.push(body)
            }
        })
        return countrys;
    }

    const [data, setData] = useState([]);
    const [dataMatch, setDataMatch] = useState([]);
    const [allData, setAllData] = useState([getAllCountrys()]);
    

    const CountryName = useRef();
    const MatchList = useRef();
    const allDataList = useRef();

    const SearchCountry = () => {
        const name = CountryName.current.value;
        if (name === '') return;
        request({
            url: `https://restcountries.eu/rest/v2/name/${name}`,
            json: true
        }, (error, response, body) => {
            if (!(404 === body['status'])){
                setData((prevData) => {
                    return [body[0]]
                });
            }else{
                body = 'Error'
                setData((prevData) => {
                    return [body]
                });
            }
        })
        CountryName.current.value = null;
    };

    const SearchMatch = () => {
        const matchL = (MatchList.current.value).replace(/ /g, '').split(',');
        setDataMatch((prevData) => {
            return []
        });
        matchL.forEach(element =>
            request({
                url: `https://restcountries.eu/rest/v2/name/${element}`,
                json: true
            }, (error, response, body) => {
                if (!(404 === body['status'])){
                    for (var i in body){
                        if (body[i]['name'].toUpperCase().includes(element.toUpperCase())){
                            setDataMatch((prevData) => {
                                return [...prevData, body[i]]
                            });
                        }
                    }
                } else{
                    body = 'Error'
                    setDataMatch((prevData) => {
                        return [body]
                    });
                }
            })   
        )
        MatchList.current.value = null;
    }

    const SearchInAllData = () => {
        let filter_data =  allDataList.current.value;
        
        setAllData((prevData) => {
            return [getAllCountrys()]
        });
        
        console.log(allData)
        console.log(Object.values(allData[0]).filter(user => user.name.toUpperCase().includes(filter_data.toUpperCase())));
        
        setAllData((prevData) => {
            return [Object.values(allData[0]).filter(user => user.name.toUpperCase().includes(filter_data.toUpperCase()))]
        });
    }

    // ROULETTE ACTIVITY 4
    const [coins, setCoins] = useState(20);
    const [winCoin, setWinCoin] = useState(0);

    let reels = {
        reel1: ["cherry", "lemon", "apple", "lemon", "banana", "banana", "lemon", "lemon"],
        reel2: ["lemon", "apple", "lemon", "lemon", "cherry", "apple", "banana", "lemon"],
        reel3: ["lemon", "apple", "lemon", "apple", "cherry", "lemon", "banana", "lemon"]
    }

    const [resultData, setResultData] = useState({
        valor1: reels['reel1'][0],
        valor2: reels['reel2'][0],
        valor3: reels['reel3'][0]
    })

    const addResult = (data) => {
        let resultSpin = {}
        setWinCoin((prevData) => {
            return 0
        })
        for (var i in data){
            if (!(data[i] in resultSpin)){
                resultSpin[data[i]] = 1
            } else{
                resultSpin[data[i]] += 1
            }
        }
        console.log(resultSpin)
        if ('cherry' in resultSpin){
            if (resultSpin['cherry'] === 3){
                setWinCoin((prevData) => {
                    return 50
                })
                setCoins((prevData) => {
                    return prevData + 50
                });
            }
            if (resultSpin['cherry'] === 2){
                setWinCoin((prevData) => {
                    return 40
                })
                setCoins((prevData) => {
                    return prevData + 40
                });
            }
        }
        if ('apple' in resultSpin){
            if (resultSpin['apple'] === 3){
                setWinCoin((prevData) => {
                    return 20
                })
                setCoins((prevData) => {
                    return prevData + 20
                });
            }
            if (resultSpin['apple'] === 2){
                setWinCoin((prevData) => {
                    return 10
                })
                setCoins((prevData) => {
                    return prevData + 10
                });
            }
        }
        if ('banana' in resultSpin){
            if (resultSpin['banana'] === 3){
                setWinCoin((prevData) => {
                    return 15
                })
                setCoins((prevData) => {
                    return prevData + 15
                });
            }
            if (resultSpin['banana'] === 2){
                setWinCoin((prevData) => {
                    return 5
                })
                setCoins((prevData) => {
                    return prevData + 5
                });
            }
        }
        if ('lemon' in resultSpin){
            if (resultSpin['lemon'] === 3){
                setWinCoin((prevData) => {
                    return 3
                })
                setCoins((prevData) => {
                    return prevData + 3
                });
            }
        }
    }

    const SpinRoulette = () => {
        setCoins((prevData) => {
            return prevData - 1
        });
        let valor1 = reels['reel1'][Math.floor(Math.random() * reels['reel1'].length)];
        let valor2 = reels['reel2'][Math.floor(Math.random() * reels['reel2'].length)];
        let valor3 = reels['reel3'][Math.floor(Math.random() * reels['reel3'].length)];
        setResultData((prevData) => {
            return {
                'valor1': valor1,
                'valor2': valor2,
                'valor3': valor3,
            }
        });
        addResult({
            'valor1': valor1,
            'valor2': valor2,
            'valor3': valor3
        })     
    }
    

    return(
        <Router>
            <div className="navBar">
                <div className="container">
                    <Link to="/act" className="menu">
                        Act 1-2-3
                    </Link>
                </div>
                <div className="container">
                    <Link to="/roulette" className="menu">
                        Act 4
                    </Link>
                </div>
            </div>
            <Switch>
                <Route path="/act">
                        <div className='blockCountry'>
                            <div>
                                <p>Introduce the name of a Country</p>
                                <input ref={CountryName} type="text" placeholder="Search Country"></input>
                                <button onClick={SearchCountry}>Search</button>
                                <DataCountry data={data} />
                            </div>
                            <br />
                            <div>
                                <p>Introduce strings delimited with comma</p>
                                <input ref={MatchList} type="text" placeholder="Search Country"></input>
                                <button onClick={SearchMatch}>Search</button>
                                <SearchMatchCountry data={dataMatch} />
                            </div>
                            <div>
                                <p>'Incomplet'search by name</p>
                                <input ref={allDataList} type="text" placeholder="Search Country"></input>
                                <button onClick={SearchInAllData}>Search</button>
                                <SearchInAllCountrys data={allData} filter={allDataList} />
                            </div>
                        </div>
                </Route>
            </Switch>
            <Switch>
                <Route path="/roulette">
                    <div className='dataUser'>
                        <div className="coins">
                            <p className="countCoins">{coins} Coins</p>
                            <p className="winCoin countCoins">Win {winCoin} Coin</p>
                            <button className="spinButton" onClick={SpinRoulette}>Spin</button>
                        </div>
                    </div>
                    <div className="roulette">
                        <p className="boxRou">{resultData['valor1']}</p>
                        <p className="boxRou">{resultData['valor2']}</p>
                        <p className="boxRou">{resultData['valor3']}</p>
                    </div>
                </Route>
            </Switch>
        </Router>
    )
}