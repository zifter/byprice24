import React from 'react';
import {render, screen} from '@testing-library/react';
import App from './App';
import {store} from './redux/store';
import {Provider} from 'react-redux';

test('renders learn react link', () => {
  render(
      <Provider store={store}>
        <App />
      </Provider>,
  );
  const linkElement = screen.getByText('2022 by zifter');
  expect(linkElement).toBeInTheDocument();
});
