import { Card } from "animal-island-ui";
import { useEffect, useState } from "react";

const SLOTS = [8, 12, 16, 20];

export default function MerchantTimeline() {
    const [remain, setRemain] = useState("");

    const [currentIndex, setCurrentIndex] = useState(0);

    function calculate() {
        const now = new Date();

        const hour = now.getHours();

        let current = 0;

        for (let i = 0; i < SLOTS.length; i++) {
            if (hour >= SLOTS[i]) {
                current = i;
            }
        }

        setCurrentIndex(current);

        let next = new Date();

        if (current === 3) {
            next.setDate(next.getDate() + 1);
            next.setHours(8, 0, 0, 0);
        } else {
            next.setHours(SLOTS[current + 1], 0, 0, 0);
        }

        const diff = Math.floor((next - now) / 1000);

        const h = String(Math.floor(diff / 3600)).padStart(2, "0");
        const m = String(Math.floor((diff % 3600) / 60)).padStart(2, "0");
        const s = String(diff % 60).padStart(2, "0");

        setRemain(`${h}:${m}:${s}`);
    }

    useEffect(() => {
        calculate();

        const timer = setInterval(calculate, 1000);

        return () => clearInterval(timer);
    }, []);

    return (
        <Card className="mb-6 p-6">

            <div className="flex justify-between items-center">

                {SLOTS.map((slot, index) => (
                    <div
                        key={slot}
                        className="flex flex-col items-center"
                    >
                        <div
                            className={`
                                h-14
                                w-14
                                rounded-full
                                border-4
                                flex
                                items-center
                                justify-center
                                font-bold
                                ${
                                index === currentIndex
                                    ? "bg-[#f6be4f] border-[#8b4513]"
                                    : "bg-[#f7f1df] border-[#c4a484]"
                            }
                            `}
                        >
                            {index <= currentIndex ? "✓" : ""}
                        </div>

                        <span className="mt-2 text-sm">
                            {slot}:00
                        </span>
                    </div>
                ))}
            </div>

            <div className="mt-6 border-t border-dashed pt-4">

                <div className="text-sm text-[#9a7f63]">
                    距下班次
                </div>

                <div className="text-4xl font-bold text-[#e56c3d]">
                    {remain}
                </div>

            </div>

        </Card>
    );
}