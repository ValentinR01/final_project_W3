<script>
  import Image from "../../atoms/Image.svelte";
  import Account from "../../../assets/img/account.png";

  /**
   * @type {any}
  */
  export let employeePicture = '';
</script>

<div class='commentary-card'>
  <div class='commentary__header'>
    <Image
      imageSrc={employeePicture ? employeePicture : Account }
      imageAlt="Employee picture"
      imageWidth=40
      imageHeight=40
      border
    />
    <div class='commentary__infos'>
      <p class="text-preset-4"> <slot name='name' /></p>
      <p class="infos__job text-preset-5"> <slot name='job' /> </p>
    </div>
    <p class="commentary__date text-preset-5"> <slot name='date' /> </p>
  </div>

  <p class="text-preset-4"> <slot name='comment' /> </p>
</div>

<style>
  .commentary-card{
    padding: var(--spacing-3) var(--spacing-4);
    background-color: var(--color-background-tercary);
    border: 1px solid var(--color-border);
    border-radius: var(--card-radius);
  }

  .commentary__header{
    display: flex;
    column-gap: var(--spacing-2);
    margin-bottom: var(--spacing-3);
  }

  .commentary__infos{
    margin-top: var(--spacing-1);
    width: calc(100% - 140px);
  }

  .infos__job, .commentary__date{
    color: var(--color-text-dark);
    margin-top: var(--spacing-1);
    text-transform: capitalize;
  }
</style>