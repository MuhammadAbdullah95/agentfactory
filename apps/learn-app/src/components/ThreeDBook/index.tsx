import React from 'react';
import styles from './styles.module.css';
import clsx from 'clsx';

interface ThreeDBookProps {
    src: string;
    alt?: string;
    className?: string;
}

export const ThreeDBook: React.FC<ThreeDBookProps> = ({ src, alt = "Book Cover", className }) => {
    const bookRef = React.useRef<HTMLDivElement>(null);
    const [rotate, setRotate] = React.useState({ x: 0, y: 0 });

    const handleMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
        if (!bookRef.current) return;

        const rect = bookRef.current.getBoundingClientRect();
        const width = rect.width;
        const height = rect.height;

        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;

        const rotateY = ((mouseX - width / 2) / width) * 30; // -15 to 15 deg
        const rotateX = ((height / 2 - mouseY) / height) * 20; // -10 to 10 deg

        setRotate({ x: rotateX, y: rotateY });
    };

    const handleMouseLeave = () => {
        setRotate({ x: 0, y: 0 });
    };

    return (
        <div
            className={clsx(styles.bookWrapper, className)}
            onMouseMove={handleMouseMove}
            onMouseLeave={handleMouseLeave}
        >
            <div
                ref={bookRef}
                className={styles.book}
                style={{
                    '--rotate-x': `${rotate.x}deg`,
                    '--rotate-y': `${rotate.y}deg`,
                } as React.CSSProperties}
            >
                {/* Front Cover */}
                <div className={styles.cover}>
                    <img src={src} alt={alt} className={styles.coverImg} />
                    {/* Dynamic Sheen */}
                    <div className={styles.sheen} />
                    <div className={styles.spineShadow} />
                </div>

                {/* Back Cover */}
                <div className={styles.back} />

                {/* Spine (Left) */}
                <div className={styles.left} />

                {/* Page Block (Top, Bottom, Right) */}
                <div className={styles.right} />
                <div className={styles.top} />
                <div className={styles.bottom} />
            </div>
        </div>
    );
};
