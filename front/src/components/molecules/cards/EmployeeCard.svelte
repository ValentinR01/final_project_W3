<script>
  import Image from "../../atoms/Image.svelte";
  import Account from "../../../assets/img/account.png";

  /**
   * @type {any}
   */
   export let employeePicture;
</script>

<div class='employee-card'>
  <Image
    imageSrc={employeePicture ? employeePicture : Account }
    imageAlt="Employee picture"
    imageWidth=55
    border
  />
  <p class="employee__name text-preset-3"> <slot name='name' /></p>
  <p class="text-preset-4">Projets en cours : <slot name='number-projects' /> </p>
</div>

<style>
  .employee-card{
    padding: var(--spacing-3);
    border: 1px solid var(--color-border);
    border-radius: var(--card-radius);
    width: 245px;
  }

  .employee-card:hover{
    border-color: var(--color-highlight);
  }

  .employee__name{
    color: var(--color-text-dark);
    margin-top: var(--spacing-3);
    margin-bottom: var(--spacing-1);
  }
</style>