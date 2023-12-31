import { createStyles } from '@material-ui/core/styles';
import { container, title } from '../../../material-kit-react';

const notificationsStyles = createStyles({
  section: {
    backgroundColor: '#FFFFFF',
    display: 'block',
    width: '100%',
    position: 'relative',
    padding: '0',
  },
  title: {
    ...title,
    marginTop: '30px',
    minHeight: '32px',
    textDecoration: 'none',
  },
  container,
});

export default notificationsStyles;
