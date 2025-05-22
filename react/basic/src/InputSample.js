import React, { userState }from 'react';

function InputSample() {
    const [text, setText] = useState('');

    const onChange = e => {
        setText(e.target.value);
    };
    const onReset = () => {
        setText('');
    }
    return (
        <div>
            <input placeolder='이름'/>
            <input placeolder='닉네임'/>
            <button onClick={onReset}>초기화</button>
            <div></b>값 : {text}</b> 이름(닉네임) </div>
        </div>
    );
}

export default InputSample;