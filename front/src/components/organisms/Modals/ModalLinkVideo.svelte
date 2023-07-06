<script>
  import { onMount } from 'svelte';
  import { writable } from 'svelte/store';

  import CopyIcon from "../../../assets/icons/CopyIcon.svelte";
  import Icon from "../../atoms/Icon.svelte";
  import Input from "../../atoms/Input.svelte";
  import Text from "../../atoms/Text.svelte";
  import ModalCard from "../../molecules/cards/ModalCard.svelte";
  import CheckIcon from '../../../assets/icons/CheckIcon.svelte';

  export let value = '';
  let copied = writable(false);

  async function copyToClipboard() {
    try {
      await navigator.clipboard.writeText(value);
      copied.set(true);
    } catch (err) {
      console.error('Failed to copy text to clipboard:', err);
    }
  }

  // Remove validation message after 2 seconds
  onMount(() => {
    copied.subscribe(value => {
      if (value) {
        setTimeout(() => {
          copied.set(false);
        }, 2000);
      }
    });
  });
</script>

<ModalCard buttonText='Ouvrir modale partage lien video'>
  <Text
    textTag='h2'
    class='text-preset-2 text--uppercase text-center'
  >
    Lien à partager
  </Text>

  <div class='video-link'>
    <Input value={value} readonly/>
    <button class="button--transparent" on:click={copyToClipboard}>
      <Icon name="copy" width=38 height=38>
        <CopyIcon />
      </Icon>
    </button>
  </div>

  {#if $copied}
    <div class='copy-message'>
      <p class='text-preset-5'>Lien copié</p>
      <Icon name='check' color='var(--color-primary)' width=10 height=10>
        <CheckIcon />
      </Icon>
    </div>
  {:else}
    <div class="copy-message--empty"></div>
  {/if}
</ModalCard>

<style>
  .video-link{
    margin-top: var(--spacing-4);
    display: flex;
    column-gap: var(--spacing-2);
  }

  .copy-message{
    display: flex;
    justify-content: center;
    column-gap: var(--spacing-1);
    margin-top: var(--spacing-2);
    color: var(--color-primary);
  }

  .copy-message--empty{
    height: 22px;
  }
</style>