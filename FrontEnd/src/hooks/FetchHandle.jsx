import { useEffect, useState } from "react";
import {fetchDataFromApiLocal} from '../util/api'

const fetchHandler = (url) => {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        setLoading("loading...")
        setData(null);
        setError(null);

        fetchDataFromApiLocal(url)
            .then((res) => {
                setLoading(false)
                if (!res) {
                    setError("Something went wrong!")
                }
                setData(res)
            })
            .catch((err) => {
                setLoading(false)
                // setError(err)
                setError("Something went wrong!")
            });
    }, [url]);

    return {data , loading , error}
}

export default fetchHandler