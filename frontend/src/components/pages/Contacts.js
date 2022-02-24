import React from 'react';
import PropTypes from 'prop-types';
import {
  Div, Text, Container,
} from 'atomize';

const TextContact = ({text, bottomValue, textSize, textWeight, tag}) => {
  return (
    <Div textAlign="left">
      <Text tag={tag || 'section'} textSize={textSize || 'paragraph'}
        textWeight={textWeight || '400'}
        m={{b: bottomValue}}>
        {text}
      </Text>
    </Div>
  );
};
TextContact.propTypes = {
  text: PropTypes.string.isRequired,
  bottomValue: PropTypes.string,
  textSize: PropTypes.string,
  textWeight: PropTypes.string,
  tag: PropTypes.string,
};
const Contacts = () => {
  return (<>
    <Container p="0" d="flex" flexDir="column" align="flex-start">
      <TextContact tag={'h1'} text={'Контакты'} textSize={'display1'}
        bottomValue={'0.5rem'} textWeight={'600'}/>
      <TextContact text={'У Вас возникли вопросы? Мы здесь чтобы помочь.'}
        bottomValue={'1.7rem'}/>
      <TextContact text={'Информация о компании:'} textSize={'heading'} />
      <TextContact text={'UAB Elektroninės prekybos centras'}
        bottomValue={'0'}/>
      <TextContact text={'Код предприятия: 304298127'}/>
      <TextContact text={'НДС код: LT100010323218'}
        bottomValue={'1.7rem'}/>
      <TextContact text={'Адрес:'} textSize={'heading'}/>
      <TextContact text={'Laisvės pr. 60-1107, LT-05120 Vilnius'}
        bottomValue={'1.7rem'}/>
      <TextContact text={'E. почта: contact@findprice.by'}/>
    </Container>
  </>
  );
};

export default Contacts;
