"use client";
import { useEffect, useState } from 'react';
import Image from "next/image";

export default function Home() {
    const [counter, setCounter] = useState<number>(0);

    useEffect(() => {}, [counter]);

    return (
        <div>
            <div className="flex flex-col items-center justify-center h-screen">
                <Image 
                    src="/graph.png" 
                    alt="Graph"
                    width={400}
                    height={400}/>
                <button onClick={() => setCounter((prevCount) => prevCount + 1)}className="text-3xl border">test</button>
                <p className="text-3xl">{counter}</p>
            </div>
        </div>
    );
};