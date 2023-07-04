import type { Meta, StoryObj } from '@storybook/svelte';

import Button from './Org.svelte';

// More on how to set up stories at: https://storybook.js.org/docs/svelte/writing-stories/introduction
const meta = {
  title: 'Organisms/Organisme name',
  component: Button,
  tags: ['autodocs'],
} satisfies Meta<Button>;

export default meta;
type Story = StoryObj<typeof meta>;

// More on writing stories with args: https://storybook.js.org/docs/svelte/writing-stories/args
export const Primary: Story = {
  args: {
    primary: true,
    label: 'Button',
  },
};

export const Secondary: Story = {
  args: {
    label: 'Button',
  },
};
