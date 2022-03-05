import React from 'react';
import {render, screen} from '@testing-library/react';
import Contacts from './Contacts';

test('renders Contact info', () => {
    render(<Contacts/>);
    const textElement = screen.getByText('Контакты');
    expect(textElement).toBeInTheDocument();

});

test('should navigate to ... when link is clicked', () => {
    const { getByTestId } = render(<a data-testid='link' href="mailto:contact@findprice.by">Click Me</a>);
    expect(getByTestId('link')).toHaveAttribute('href', 'mailto:contact@findprice.by');
});
